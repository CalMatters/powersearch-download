import click
import requests
from .powersearch import create_contribution_download_url, create_ie_download_url

_DEFAULT_USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36'

@click.command()
@click.option('-t', '--data-type', default='contributions', help="Can be \"contributions\" or \"ie\"\nDefault: contributions")
@click.option('--candidate', default=None, help="Candidate name (LAST, FIRST)")
@click.option('--committee', default=None, help="Limit data to one specific committee")
@click.option('-e', '--election-cycle', default=None, multiple=True, help="Election cycles in YYYY-YYYY format")
@click.option('-m', '--measures', default=None, multiple=True, help="Limit data to specific ballot measures")
@click.option('--office', default=None, help="Office such as 'Governor', 'Secretary of State', or 'State Assembly'")
@click.option('--output', default="powersearch-dl_data.csv", help="Output file path")
@click.option('--position', default=None, help="Limit independent expenditure data to one particular position (S or O; support or oppose)")
@click.option('-s', '--silent', is_flag=True, default=False, help="Do not error regardless of query")
@click.option('--user-agent', default=_DEFAULT_USER_AGENT, help="User-Agent HTTP header for request to PowerSearch\nDefault: %s" % _DEFAULT_USER_AGENT)
@click.option('-v', '--verbose', is_flag=True, default=False, help="Show extra information")
def cli(data_type, candidate, committee, election_cycle, measures, office, output, position, silent, user_agent, verbose):
    """Download campaign contribution or independent expenditure data from California secretary of state's tool called PowerSearch"""
    url = None

    if data_type == 'contributions':
        url = create_contribution_download_url(candidate, office, election_cycle, measures)
    elif data_type == 'ie':
        url = create_ie_download_url(election_cycle, committee, position, candidate, office, measures)
    elif not silent:
        raise click.ClickException('Data type parameter needs to be either "contributions" or "ie"\n"%s" is not supported' % data_type)
    
    if verbose:
        print('📂 Downloading data from %s' % url)

    r = requests.get(url, allow_redirects=True, headers={
         "Accept-Language": "en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7",
         "Referer": "https://powersearch.sos.ca.gov/advanced.php",
         "User-Agent": user_agent,
    })
    lines = r.text.split('\n')
    lines_without_footer = lines[0:-8]
    lines_without_footer_count = len(lines_without_footer)
    
    is_bad_contributions_query = data_type == 'contributions' and lines[0] == ""
    is_empty_ie_query = data_type == 'ie' and lines[1] == ""
    
    if (is_bad_contributions_query or is_empty_ie_query) and not silent: # bad query and no data returned
        raise click.ClickException('''Query returned zero rows of data
\nCould be because:
* There's no matching data
* It's a bad query
* The request was blocked by bot
* The request returned too much data and needs to be further filtered
''')
    
    with open(output, 'w') as f:
        f.write('\n'.join(lines_without_footer))

    if not silent:
        print(f"✅ Saved {lines_without_footer_count:,} rows to %s" % output)
