from powersearchdownload.powersearch import create_contribution_download_url, create_ie_download_url, _serialize_list, _serialize_dict

def test__serialize_list():
  _EXPECTED = 'a:2:{i:0;s:4:"key1";i:1;s:4:"key2";}'
  values = {"key1": "value1", "key2": "value2"}
  actual = _serialize_list(values)
  assert actual == _EXPECTED
  
def test__serialize_dict():
  _EXPECTED = 'a:2:{s:4:"key1";s:6:"value1";s:4:"key2";s:6:"value2";}'
  values = {"key1": "value1", "key2": "value2"}
  actual = _serialize_dict(values)
  assert actual == _EXPECTED

def test_create_download_url_for_contributions_beccerra():
  _EXPECTED = '''https://powersearch.sos.ca.gov/download_csv.php?w=WHERE+smry_candidates.RecipientCandidateNameNormalized+%3D+%3F+AND+contributions_search.CandidateContribution+%3D+%27Y%27&d=a%3A1%3A%7Bi%3A0%3Bs%3A15%3A%22BECERRA%2C+XAVIER%22%3B%7D&c=a%3A4%3A%7Bs%3A16%3A%2200Contributor%28s%29%22%3Bs%3A3%3A%22All%22%3Bs%3A19%3A%2201Contributor_State%22%3Bs%3A3%3A%22All%22%3Bs%3A14%3A%2202Recipient%28s%29%22%3Bs%3A26%3A%22Candidate%3A+BECERRA%2C+XAVIER%22%3Bs%3A31%3A%2207Contribution_Dates_and_Cycles%22%3Bs%3A3%3A%22All%22%3B%7D'''
  actual = create_contribution_download_url(candidate="Becerra, Xavier")
  assert actual == _EXPECTED

def test_create_download_url_for_contributions_beccerra_gov():
  _EXPECTED = '''https://powersearch.sos.ca.gov/download_csv.php?w=WHERE+smry_candidates.RecipientCandidateNameNormalized+%3D+%3F+AND+smry_offices.RecipientCandidateOffice+%3D+%3F+AND+contributions_search.CandidateContribution+%3D+%27Y%27&d=a%3A2%3A%7Bi%3A0%3Bs%3A15%3A%22BECERRA%2C+XAVIER%22%3Bi%3A1%3Bs%3A8%3A%22Governor%22%3B%7D&c=a%3A5%3A%7Bs%3A16%3A%2200Contributor%28s%29%22%3Bs%3A3%3A%22All%22%3Bs%3A19%3A%2201Contributor_State%22%3Bs%3A3%3A%22All%22%3Bs%3A14%3A%2202Recipient%28s%29%22%3Bs%3A26%3A%22Candidate%3A+BECERRA%2C+XAVIER%22%3Bs%3A31%3A%2207Contribution_Dates_and_Cycles%22%3Bs%3A3%3A%22All%22%3Bs%3A18%3A%2203Recipient_Office%22%3Bs%3A8%3A%22Governor%22%3B%7D'''
  actual = create_contribution_download_url(candidate="Becerra, Xavier", office="Governor")
  assert actual == _EXPECTED
  
def test_create_download_url_for_contributions_state_assembly_2025_2026():
  _EXPECTED = '''https://powersearch.sos.ca.gov/download_csv.php?w=WHERE+smry_offices.RecipientCandidateOffice+%3D+%3F+AND+contributions_search.CandidateContribution+%3D+%27Y%27+AND+%28contributions_search.ElectionCycle+%3D+%3F%29&d=a%3A2%3A%7Bi%3A0%3Bs%3A14%3A%22State+Assembly%22%3Bi%3A1%3Bs%3A4%3A%222025%22%3B%7D&c=a%3A6%3A%7Bs%3A16%3A%2200Contributor%28s%29%22%3Bs%3A3%3A%22All%22%3Bs%3A19%3A%2201Contributor_State%22%3Bs%3A3%3A%22All%22%3Bs%3A14%3A%2202Recipient%28s%29%22%3Bs%3A14%3A%22All+candidates%22%3Bs%3A31%3A%2207Contribution_Dates_and_Cycles%22%3Bs%3A0%3A%22%22%3Bs%3A18%3A%2203Recipient_Office%22%3Bs%3A14%3A%22State+Assembly%22%3Bs%3A21%3A%2209Contribution_Cycles%22%3Bs%3A4%3A%222025%22%3B%7D'''
  actual = create_contribution_download_url(office="State Assembly", election_cycles=["2025-2026"])
  assert actual == _EXPECTED
  
def test_create_download_url_for_contributions_sos():
  _EXPECTED = '''https://powersearch.sos.ca.gov/download_csv.php?w=WHERE+smry_offices.RecipientCandidateOffice+%3D+%3F+AND+contributions_search.CandidateContribution+%3D+%27Y%27&d=a%3A1%3A%7Bi%3A0%3Bs%3A18%3A%22Secretary+of+State%22%3B%7D&c=a%3A5%3A%7Bs%3A16%3A%2200Contributor%28s%29%22%3Bs%3A3%3A%22All%22%3Bs%3A19%3A%2201Contributor_State%22%3Bs%3A3%3A%22All%22%3Bs%3A14%3A%2202Recipient%28s%29%22%3Bs%3A14%3A%22All+candidates%22%3Bs%3A31%3A%2207Contribution_Dates_and_Cycles%22%3Bs%3A3%3A%22All%22%3Bs%3A18%3A%2203Recipient_Office%22%3Bs%3A18%3A%22Secretary+of+State%22%3B%7D'''
  actual = create_contribution_download_url(office='Secretary of State')
  assert actual == _EXPECTED
  
def test_create_download_url_for_contributions_ballot_measures_2023_2024():
  _EXPECTED = '''https://powersearch.sos.ca.gov/download_csv.php?w=WHERE+contributions_search.BallotMeasureContribution+%3D+%27Y%27+AND+%28contributions_search.ElectionCycle+%3D+%3F%29&d=a%3A1%3A%7Bi%3A0%3Bs%3A4%3A%222023%22%3B%7D&c=a%3A6%3A%7Bs%3A16%3A%2200Contributor%28s%29%22%3Bs%3A3%3A%22All%22%3Bs%3A19%3A%2201Contributor_State%22%3Bs%3A3%3A%22All%22%3Bs%3A14%3A%2202Recipient%28s%29%22%3Bs%3A19%3A%22All+ballot+measures%22%3Bs%3A31%3A%2207Contribution_Dates_and_Cycles%22%3Bs%3A0%3A%22%22%3Bs%3A27%3A%2206Exclude_Allied_Committees%22%3Bs%3A2%3A%22No%22%3Bs%3A21%3A%2209Contribution_Cycles%22%3Bs%3A4%3A%222023%22%3B%7D'''
  actual = create_contribution_download_url(ballot_measures="All ballot measurers", election_cycles=["2023-2024"]) 
  assert actual == _EXPECTED
  
def test_create_download_url_for_contributions_insurance_commissioner_2015_2016_2019_2020():
  _EXPECTED = '''https://powersearch.sos.ca.gov/download_csv.php?w=WHERE+smry_offices.RecipientCandidateOffice+%3D+%3F+AND+contributions_search.CandidateContribution+%3D+%27Y%27+AND+%28contributions_search.ElectionCycle+%3D+%3F+OR+contributions_search.ElectionCycle+%3D+%3F%29&d=a%3A3%3A%7Bi%3A0%3Bs%3A22%3A%22Insurance+Commissioner%22%3Bi%3A1%3Bs%3A4%3A%222019%22%3Bi%3A2%3Bs%3A4%3A%222015%22%3B%7D&c=a%3A6%3A%7Bs%3A16%3A%2200Contributor%28s%29%22%3Bs%3A3%3A%22All%22%3Bs%3A19%3A%2201Contributor_State%22%3Bs%3A3%3A%22All%22%3Bs%3A14%3A%2202Recipient%28s%29%22%3Bs%3A14%3A%22All+candidates%22%3Bs%3A31%3A%2207Contribution_Dates_and_Cycles%22%3Bs%3A0%3A%22%22%3Bs%3A18%3A%2203Recipient_Office%22%3Bs%3A22%3A%22Insurance+Commissioner%22%3Bs%3A21%3A%2209Contribution_Cycles%22%3Bs%3A10%3A%222019%2C+2015%22%3B%7D'''
  actual = create_contribution_download_url(office="Insurance Commissioner", election_cycles=['2015-2016', '2019-2020'])
  assert actual == _EXPECTED
  
def test_create_download_url_for_contributions_january_2026():
  _EXPECTED = '''https://powersearch.sos.ca.gov/download_csv.php?w=WHERE+%28contributions_search.TransactionDateEnd+%3E%3D+%3F+AND+contributions_search.TransactionDateEnd+%3C%3D+%3F%29&d=a%3A2%3A%7Bi%3A0%3Bs%3A10%3A%222026-01-01%22%3Bi%3A1%3Bs%3A10%3A%222026-01-31%22%3B%7D&c=a%3A5%3A%7Bs%3A16%3A%2200Contributor%28s%29%22%3Bs%3A3%3A%22All%22%3Bs%3A19%3A%2201Contributor_State%22%3Bs%3A3%3A%22All%22%3Bs%3A14%3A%2202Recipient%28s%29%22%3Bs%3A3%3A%22All%22%3Bs%3A31%3A%2207Contribution_Dates_and_Cycles%22%3Bs%3A0%3A%22%22%3Bs%3A20%3A%2208Contribution_Dates%22%3Bs%3A23%3A%222026-01-01+-+2026-01-31%22%3B%7D'''
  actual = create_contribution_download_url(from_date="2026-01-01", to_date="2026-01-31")
  assert actual == _EXPECTED

# IE
def test_create_download_url_for_ie_all():
  _EXPECTED = '''https://powersearch.sos.ca.gov:3000/ie/csvDownload?'''
  actual = create_ie_download_url()
  assert actual == _EXPECTED

def test_create_download_url_for_ie_specific_committee():
  _EXPECTED = '''https://powersearch.sos.ca.gov:3000/ie/csvDownload?expendername=Mobilizing%20Economic%20Transformation%20Across%20(Meta)%20California&'''
  actual = create_ie_download_url(committee="Mobilizing Economic Transformation Across (Meta) California")
  assert actual == _EXPECTED

def test_create_download_url_for_ie_specific_stance():
  _EXPECTED = '''https://powersearch.sos.ca.gov:3000/ie/csvDownload?stance=S&'''
  actual = create_ie_download_url(position="S")
  assert actual == _EXPECTED

def test_create_download_url_for_ie_specific_candidate():
  _EXPECTED = '''https://powersearch.sos.ca.gov:3000/ie/csvDownload?candidatename=Becerra,%20Xavier&'''
  actual = create_ie_download_url(candidate="Becerra, Xavier")
  assert actual == _EXPECTED

def test_create_download_url_for_ie_specific_office():
  _EXPECTED = '''https://powersearch.sos.ca.gov:3000/ie/csvDownload?candidateoffice=Attorney%20General&'''
  actual = create_ie_download_url(office="Attorney General")
  assert actual == _EXPECTED
  
def test_create_download_url_for_ie_specific_ballot_measure():
  _EXPECTED = 'https://powersearch.sos.ca.gov:3000/ie/csvDownload?propositionname=Prop%2050%20-%20ACA%208%20(RIVAS)%20CONGRESSIONAL%20REDISTRICTING.%20(RES.%20CH.%20156,%202025)&'
  actual = create_ie_download_url(measures=["Prop 50 - ACA 8 (RIVAS) CONGRESSIONAL REDISTRICTING. (RES. CH. 156, 2025)"])
  assert actual == _EXPECTED
  
def test_create_download_url_for_ie_ballot_measures_2025_2026():
  _EXPECTED = '''https://powersearch.sos.ca.gov:3000/ie/csvDownload?electioncycle=2025&'''
  actual = create_ie_download_url(election_cycles=['2025-2026'])
  assert actual == _EXPECTED
  
def test_create_download_url_for_ie_ballot_measures_2021_2022_2025_2026():
  _EXPECTED = '''https://powersearch.sos.ca.gov:3000/ie/csvDownload?electioncycle=2025,2021&'''
  actual = create_ie_download_url(election_cycles=['2021-2022', '2025-2026'])
  assert actual == _EXPECTED