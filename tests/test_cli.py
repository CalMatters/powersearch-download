from click.testing import CliRunner
from powersearchdownload.cli import cli

def test_cli_contributions_success():
  runner = CliRunner()
  result = runner.invoke(cli, ['-t', 'contributions', '--candidate', 'Becerra, Xavier', '--office', 'Governor', '--election-cycle', '2025-2026'])
  assert result.exit_code == 0, '✅ Saved' in result.output
  
def test_cli_contributions_failure():
  runner = CliRunner()
  result = runner.invoke(cli, ['-t', 'contributions']) # this should be too big of a query for powersearch and result in a failure
  assert result.exit_code == 1