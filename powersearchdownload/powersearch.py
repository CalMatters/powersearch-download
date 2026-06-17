"""
powersearch.py

Utilities for building download URLs for the California SOS PowerSearch tool
to get campaign contributions or indepedent expenditures

https://powersearch.sos.ca.gov/
"""

from urllib.parse import quote, quote_plus


# ---------------------------------------------------------------------------
# PHP serialize helpers
# ---------------------------------------------------------------------------

def _serialize_list(values: dict) -> str:
    """
    Serialize the *keys* of a dict as a PHP indexed array (i:N => s:LEN:"key").

    Example:
        {"key1": "value1", "key2": "value2"}
        -> 'a:2:{i:0;s:4:"key1";i:1;s:4:"key2";}'
    """
    items = ""
    for idx, key in enumerate(values):
        items += f'i:{idx};s:{len(key)}:"{key}";'
    return f'a:{len(values)}:{{{items}}}'


def _serialize_dict(values: dict) -> str:
    """
    Serialize a dict as a PHP associative array (s:LEN:"key" => s:LEN:"val").

    Example:
        {"key1": "value1", "key2": "value2"}
        -> 'a:2:{s:4:"key1";s:6:"value1";s:4:"key2";s:6:"value2";}'
    """
    items = ""
    for key, val in values.items():
        items += f's:{len(key)}:"{key}";s:{len(val)}:"{val}";'
    return f'a:{len(values)}:{{{items}}}'


# ---------------------------------------------------------------------------
# Create URLs to download contribution data
# ---------------------------------------------------------------------------

def create_contribution_download_url(
    candidate: str | None = None,
    office: str | None = None,
    election_cycles: list | None = None,
    ballot_measures: str | None = None,
) -> str:
    """
    Build a PowerSearch CSV download URL.

    Parameters
    ----------
    candidate : str, optional
        Candidate name in "Last, First" format (stored as uppercase).
    office : str, optional
        Office name, e.g. "Governor", "State Assembly", "Secretary of State".
    election_cycles : list, optional
        List of election cycle strings in "YYYY-YYYY" format,
        e.g. ["2025-2026"] or ["2015-2016", "2019-2020"].
        Only the first year of each cycle is used, sorted descending.
    ballot_measures : str, optional
        When provided, switches to ballot-measure mode instead of candidate mode.
    """
    base = "https://powersearch.sos.ca.gov/download_csv.php"

    # Normalise inputs
    candidate_upper = candidate.upper() if candidate else None

    # Extract and sort cycle years descending (e.g. ["2019-2020","2015-2016"] -> ["2019","2015"])
    cycle_years: list[str] = []
    if election_cycles:
        cycle_years = sorted(
            [ec.split("-")[0] for ec in election_cycles],
            reverse=True,
        )

    # ------------------------------------------------------------------
    # Build WHERE clause (w) and positional data list (d)
    # ------------------------------------------------------------------
    where_parts: list[str] = []
    d_values: list[str] = []

    if ballot_measures:
        where_parts.append("contributions_search.BallotMeasureContribution = 'Y'")
    else:
        if candidate_upper:
            where_parts.append("smry_candidates.RecipientCandidateNameNormalized = ?")
            d_values.append(candidate_upper)

        if office:
            where_parts.append("smry_offices.RecipientCandidateOffice = ?")
            d_values.append(office)

        where_parts.append("contributions_search.CandidateContribution = 'Y'")

    if cycle_years:
        if len(cycle_years) == 1:
            where_parts.append("(contributions_search.ElectionCycle = ?)")
        else:
            or_clause = " OR ".join(
                "contributions_search.ElectionCycle = ?" for _ in cycle_years
            )
            where_parts.append(f"({or_clause})")
        d_values.extend(cycle_years)

    where_clause = "WHERE " + " AND ".join(where_parts)

    # d param: PHP indexed array of positional values
    d_serialized = _serialize_list({v: None for v in d_values})

    # ------------------------------------------------------------------
    # Build caption/context dict (c)
    # ------------------------------------------------------------------
    c: dict[str, str] = {}

    c["00Contributor(s)"] = "All"
    c["01Contributor_State"] = "All"

    if ballot_measures:
        c["02Recipient(s)"] = "All ballot measures"
    elif candidate_upper:
        c["02Recipient(s)"] = f"Candidate: {candidate_upper}"
    else:
        c["02Recipient(s)"] = "All candidates"

    c["07Contribution_Dates_and_Cycles"] = "" if cycle_years else "All"

    if ballot_measures:
        c["06Exclude_Allied_Committees"] = "No"
    elif office:
        c["03Recipient_Office"] = office

    if cycle_years:
        c["09Contribution_Cycles"] = ", ".join(cycle_years)

    c_serialized = _serialize_dict(c)

    # ------------------------------------------------------------------
    # Encode and assemble
    # ------------------------------------------------------------------
    w_encoded = quote_plus(where_clause)
    d_encoded = quote_plus(d_serialized)
    c_encoded = quote_plus(c_serialized)

    return f"{base}?w={w_encoded}&d={d_encoded}&c={c_encoded}"

# ---------------------------------------------------------------------------
# Create URLs to download independent expenditure data
# ---------------------------------------------------------------------------
def create_ie_download_url(
    election_cycles: list | None = None,
    committee: str | None = None,
    position: str | None = None,
    candidate: str | None = None,
    office: str | None = None,
    measures: list | None = None,
) -> str:

    base = "https://powersearch.sos.ca.gov:3000/ie/csvDownload"
    _enc = lambda v: quote(v, safe="(),")

    params = ""
    if committee:
        params += f"expendername={_enc(committee)}&"
    if position:
        params += f"stance={_enc(position)}&"
    if candidate:
        params += f"candidatename={_enc(candidate)}&"
    if office:
        params += f"candidateoffice={_enc(office)}&"
    if measures:
        params += f"propositionname={','.join(_enc(m) for m in measures)}&"
    if election_cycles:
        cycle_years = sorted(
            [ec.split("-")[0] for ec in election_cycles],
            reverse=True,
        )
        params += f"electioncycle={','.join(cycle_years)}&"

    return f"{base}?{params}"
