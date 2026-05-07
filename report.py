from executor import process_plan_item
from planner import create_plan

def generate_report(results):

    html = """
    <html>
    <head><title>Data Report</title></head>
    <body>
    <h1>Datu analīzes atskaite</h1>
    """

    for r in results:

        html += f"""
        <h2>{r['title']}</h2>
        <img src="{r['image']}" width="400">
        <p><b>SQL:</b> {r['sql']}</p>
        <hr>
        """

    html += "</body></html>"

    with open("report.html", "w", encoding="utf-8") as f:
        f.write(html)