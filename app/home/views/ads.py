from app.home.blueprint import home_bp


@home_bp.route("/ads.txt")
def ads_txt():
    return "google.com, pub-7852193310298972, DIRECT, f08c47fec0942fa0"
