# powersearch-download

A CLI tool to download campaign contribution data from [PowerSearch](https://powersearch.sos.ca.gov), a tool published by the California Secretary of State.

**Note:** This tool is currently a prototype and may not be further developed.

Please note that any text fields such as canidate names, committee names, offices, or ballot measure titles come from PowerSearch. Additionally, there are subtle differences between PowerSearch's interface for contributions and for independent expenditures so take care to match the correct one.

```sh
Usage: powersearch-download [OPTIONS]

  Download campaign contribution or independent expenditure data from
  California secretary of state's tool called PowerSearch

Options:
  -t, --data-type TEXT        Can be "contributions" or "ie" Default:
                              contributions
  --candidate TEXT            Candidate name
  --committee TEXT            Limit data to one specific committee
  -e, --election-cycle TEXT  Election cycles in YYYY-YYYY format
  -m, --measures TEXT         Limit data to specific ballot measures
  --office TEXT               Office such as 'Governor', 'Secretary of State',
                              or 'State Assembly'
  --output TEXT               Output file path
  --position TEXT             Limit independent expenditure data to one
                              particular position (S or O; support or oppose)
  -s, --silent                Do not error regardless of query
  --user-agent TEXT           User-Agent HTTP header for request to
                              PowerSearch Default: Mozilla/5.0 (Macintosh;
                              Intel Mac OS X 10_15_7) AppleWebKit/537.36
                              (KHTML, like Gecko) Chrome/146.0.0.0
                              Safari/537.36
  -v, --verbose               Show extra information
  --help                      Show this message and exit.
```

## Examples

### Contributions

Download all contributions to Xavier Becerra in his gubernatorial campaign

`powersearch-download -t contributions --candidate "Becerra, Xavier" --office Governor`

Download all contributions to State Assembly candidates in the 2025-2026 cycle

`powersearch-download -t contributions --office "State Assembly" --election-cycle 2025-2026`

### Independent expenditures

Download all independent expenditures spent against Tom Steyer in 2025-2026

`powersearch-download -t ie --candidate "Steyer, Tom" --position O --election-cycle 2025-2026`

Download all independent expenditures in the last three cycles

`powersearch-download -t ie --election-cycle 2025-2026 --election-cycle 2023-2024 --election-cycle 2021-2022`

## Installation

You can install the CLI tool from this Github repository using `pip` or `uv`:

```sh
pip install git+https://github.com/CalMatters/powersearch-download.git
```

```sh
uv pip install "git+https://github.com/CalMatters/powersearch-download.git"
```

## Motivation

We made this tool because we needed it to regularly download contribution data from PowerSearch in our workflows and this tool does two main things:
1. Makes it easier to construct queries
2. Errors out if there is a problem with the downloaded data

And we're sharing it publicly in case other folks need it or have ideas for improvement.

## Please let us know if you use this tool!

If you end up using this tool, please get in touch and share your use case with us by sending an email to jeremia@calmatters.org.