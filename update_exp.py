import datetime
from dateutil.relativedelta import relativedelta
import re
import urllib.parse

# 1. Calculate the exact time difference
start_date = datetime.date(2011, 12, 20)
today = datetime.date.today()
diff = relativedelta(today, start_date)

# 2. Format the string (e.g., "14 years 4 months 12 days")
badge_text = f"{diff.years} years {diff.months} months {diff.days} days"

# 3. URL-encode the text for Shields.io
encoded_text = urllib.parse.quote(badge_text)
badge_url = f"https://img.shields.io/badge/Experience-{encoded_text}-0A66C2?style=for-the-badge"
markdown_badge = f"![Experience]({badge_url})"

# 4. Read the current README.md
with open("README.md", "r", encoding="utf-8") as f:
    readme = f.read()

# 5. Swap out the old badge for the newly calculated one
updated_readme = re.sub(
    r"<!-- EXP_START -->.*?<!-- EXP_END -->",
    f"<!-- EXP_START -->\n{markdown_badge}\n<!-- EXP_END -->",
    readme,
    flags=re.DOTALL
)

# 6. Save the changes
with open("README.md", "w", encoding="utf-8") as f:
    f.write(updated_readme)
