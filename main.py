from planner import create_plan
from executor import process_plan_item
from report import generate_report

context = "Analizēt klientu un pārdošanas datus"

plan = create_plan(context)

results = []

for i, item in enumerate(plan):
    results.append(process_plan_item(item, i))

generate_report(results)

print("Report generated: report.html")