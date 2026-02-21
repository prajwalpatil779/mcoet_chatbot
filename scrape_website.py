import requests
from bs4 import BeautifulSoup
import json
import time

# All important pages from MCOET website
urls = [
    "https://mcoet.mauligroup.org/home/",
    "https://mcoet.mauligroup.org/about-us/",
    "https://mcoet.mauligroup.org/chairmans-message/",
    "https://mcoet.mauligroup.org/principals-message/",
    "https://mcoet.mauligroup.org/vision-mission-institute/",
    "https://mcoet.mauligroup.org/academic-programmes/",
    "https://mcoet.mauligroup.org/scheme-and-syllabus/",
    "https://mcoet.mauligroup.org/academic-calendar-2/",
    "https://mcoet.mauligroup.org/scholarships-rewards/",
    "https://mcoet.mauligroup.org/computer-science-engineering/",
    "https://mcoet.mauligroup.org/information-technology/",
    "https://mcoet.mauligroup.org/electronic-telecomm/",
    "https://mcoet.mauligroup.org/electrical-engineering/",
    "https://mcoet.mauligroup.org/mechanical-engineering/",
    "https://mcoet.mauligroup.org/civil-engineering/",
    "https://mcoet.mauligroup.org/applied-sciences-and-humanities/",
    "https://mcoet.mauligroup.org/master-of-engineering-digital-electronics/",
    "https://mcoet.mauligroup.org/master-of-engineering-e-p-s/",
    "https://mcoet.mauligroup.org/campus-facilities/",
    "https://mcoet.mauligroup.org/library/",
    "https://mcoet.mauligroup.org/transportation/",
    "https://mcoet.mauligroup.org/infrastructure/",
    "https://mcoet.mauligroup.org/about-t-p/",
    "https://mcoet.mauligroup.org/our-recruiters/",
    "https://mcoet.mauligroup.org/tandp-placement/",
    "https://mcoet.mauligroup.org/career-guidance-cell/",
    "https://mcoet.mauligroup.org/anti-ragging/",
    "https://mcoet.mauligroup.org/grievance-redressal/",
    "https://mcoet.mauligroup.org/research-promotion-cell/",
    "https://mcoet.mauligroup.org/ph-d-cell/",
    "https://mcoet.mauligroup.org/iic/",
    "https://mcoet.mauligroup.org/iste/",
    "https://mcoet.mauligroup.org/about-nss/",
    "https://mcoet.mauligroup.org/green-initiatives/",
    "https://mcoet.mauligroup.org/fra-fee-structure/",
    "https://mcoet.mauligroup.org/recruitment/",
    "https://mcoet.mauligroup.org/office-administration-staff/",
    "https://mcoet.mauligroup.org/code-of-conduct/",
    "https://mcoet.mauligroup.org/value-added-courses/",
    "https://mcoet.mauligroup.org/student-cie-scheme/",
]

all_text = []

for url in urls:
    try:
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(url, headers=headers, timeout=15)
        soup = BeautifulSoup(response.text, "html.parser")
        for tag in soup(["script", "style", "nav", "footer", "header"]):
            tag.decompose()
        text = soup.get_text(separator="\n")
        text = "\n".join([line.strip() for line in text.splitlines() if line.strip()])
        if len(text) > 100:
            all_text.append({"source": url, "content": text})
            print(f"✅ Done: {url}")
        else:
            print(f"⚠️  Empty: {url}")
        time.sleep(1)
    except Exception as e:
        print(f"❌ Failed: {url} → {e}")

with open("college_data.json", "w", encoding="utf-8") as f:
    json.dump(all_text, f, ensure_ascii=False, indent=2)

print(f"\n🎉 Scraped {len(all_text)} pages. Saved to college_data.json")
