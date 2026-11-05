
from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.models import (
    initialize_database,
    add_website,
    get_websites,
    save_monitoring_result,
    get_monitoring_history,
    get_dashboard_stats,
    get_monitoring_stats,
    get_response_time_data
)
from app.monitor import check_website, validate_url

main = Blueprint("main", __name__)

initialize_database()




@main.route("/")
def index():
    websites = get_websites()
    stats = get_dashboard_stats()

    for website in websites:
        website["stats"] = get_monitoring_stats(website["id"])
        website["response_data"] = get_response_time_data(website["id"])

    return render_template(
        "index.html",
        websites=websites,
        stats=stats
    )




@main.route("/add", methods=["POST"])
def add():
    url = request.form.get("url", "").strip()

    if not validate_url(url):
        flash("Please enter a valid HTTP or HTTPS URL.")
        return redirect(url_for("main.index"))

    website_id = add_website(url)

    if website_id is None:
        flash("This website is already being monitored.")
        return redirect(url_for("main.index"))

    flash("Website added successfully!")
    return redirect(url_for("main.index"))


@main.route("/check/<int:website_id>", methods=["POST"])
def check(website_id):
    websites = get_websites()
    website = next(
        (site for site in websites if site["id"] == website_id),
        None
    )

    if website is None:
        flash("Website not found.")
        return redirect(url_for("main.index"))

    result = check_website(website["url"])
    save_monitoring_result(website_id, result)

    flash(f"Check completed: {result['status']}")
    return redirect(url_for("main.index"))


@main.route("/history/<int:website_id>")
def history(website_id):
    websites = get_websites()
    website = next(
        (site for site in websites if site["id"] == website_id),
        None
    )

    if website is None:
        flash("Website not found.")
        return redirect(url_for("main.index"))

    records = get_monitoring_history(website_id)
    return render_template(
        "history.html",
        website=website,
        records=records
    )
