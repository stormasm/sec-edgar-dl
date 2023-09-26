from sec_edgar_downloader import Downloader

# Initialize a downloader instance. Download filings to the current
# working directory. Must declare company name and email address
# to form a user-agent string that complies with the SEC Edgar's
# programmatic downloading fair access policy.
# More info: https://www.sec.gov/os/webmaster-faq#code-support
# Company name and email are used to form a user-agent of the form:
# User-Agent: <Company Name> <Email Address>
dl = Downloader("MyCompanyName", "my.email@domain.com")

# Get all 10-K filings for
#dl.get("10-K", "AVGO")

# Get the latest 10-K filings for
dl.get("10-K", "AVGO", limit=3)

# Get all 10-Q filings for
#dl.get("10-Q", "UI")

# Get the latest 10-Q filings for
dl.get("10-Q", "AVGO", limit=8)
