@app.route("/logout")
@login_required
def logout():
    resp = app.blueprints[github].get('/authorizations')
    authlist = resp.json()
    client_id = str(authlist['app']['client_id'])
    token = str(authlist['token'])
    if resp.ok:
        github.delete('/applications/:client_id/grants/:token')
        logout_user()
        flash("You have logged out")
    return redirect(url_for("index")) 

