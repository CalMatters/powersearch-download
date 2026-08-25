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

## Data Dictionary

The output data of this tool is downloaded, unmodified data from California's [Powersearch tool](https://powersearch.sos.ca.gov).

<table>
  <thead>
    <tr>
      <th>Field</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
   <tr>
<td>Recipient Name</td>
<td>
Name of the candidate associated with the committee (applies only to candidate committees)</td>
</tr>
<tr>
<td>Recipient Committee</td>
<td>
Name of the committee receiving the contribution</td>
</tr>
<tr>
<td>Recipient Committee ID</td>
<td>
The committee ID# of the recipient committee</td>
</tr>
<tr>
<td>Office Sought</td>
<td>
The office sought by a particular candidate (applies only to candidate committees). Note that this field may contain the office held by a particular candidate if he/she filled out the form as such</td>
</tr>
<tr>
<td>Ballot Measure(s)</td>
<td>
Name(s) of the ballot measure(s) and the position taken on them (supported or opposed) by a particular recipient committee. Note that one contribution to a multi-measure committee will show each measure supported or opposed by that committee</td>
</tr>
<tr>
<td>Contributor Name</td>
<td>
The name of the contributor as provided by the recipient committee in their filings</td>
</tr>
<tr>
<td>Contributor ID</td>
<td>
The official committee ID# of the contributor (if it exists and is reported), as provided by the recipient committee</td>
</tr>
<tr>
<td>Amount</td>
<td>
The amount of the contribution</td>
</tr>
<tr>
<td>Date</td>
<td>
The date on which the contribution was received</td>
</tr>
<tr>
<td>Contributor Employer</td>
<td>
the employer of the contributor usually applies only to individuals/employees</td>
</tr>
<tr>
<td>Contributor Occupation</td>
<td>
The occupation of the contributor, usually applies only to individuals/employees</td>
</tr>
<tr>
<td>Contributor State</td>
<td>
The state in which the contributor is situated</td>
</tr>
<tr>
<td>District</td>
<td>
The district in which a candidate is running (applies only to candidates for State Senate and Assembly)</td>
</tr>
<tr>
<td>Contributor Zip Code</td>
<td>
The zip code in which the contributor is situated</td>
</tr>
<tr>
<td>Contributor City</td>
<td>
The city in which the contributor is situated</td>
</tr>
<tr>
<td>Transaction Type</td>
<td>
The type of contribution; can be a monetary contribution, non-monetary contribution, or a loan</td>
</tr>
<tr>
<td>Election</td>
<td>
The specific election date for which the candidate or measure will be on the ballot</td>
</tr>
<tr>
<td>Cycle</td>
<td>
The First Year (odd) of the two-year period in which the contribution is made . For example, the 2013 cycle is 2013-2014 period</td>
</tr>
  </tbody>
</table>

## Motivation

We made this tool because we needed it to regularly download contribution data from PowerSearch in our workflows and this tool does two main things:
1. Makes it easier to construct queries
2. Errors out if there is a problem with the downloaded data

We use this tool to build our [2026 California voter guide](https://calmatters.org/california-voter-guide-2026/) and we're sharing it publicly in case other folks need it or have ideas for improvement.

## Data use
While the contents of this repo are shared under an Apache 2.0 license, CalMatters/The Markup would appreciate any credit or attribution you're willing to give. We're also interested to learn how you used it, so feel free to send us a message or open an issue if you do. If you have any questions, feel free to contact us as well.

CalMatters is a nonpartisan, nonprofit journalism venture committed to explaining how California’s state Capitol works and why it matters.

## License
Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License. There is a full copy of [the License](https://github.com/CalMatters/powersearch-download/blob/main/LICENSE) in this repository.

