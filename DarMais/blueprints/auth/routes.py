from blueprints.auth import auth_bp

@auth_bp.route('/login')
def login():
    pass

@auth_bp.route('/logout')
def logout():
    pass

@auth_bp.route('/cadastro')
def register():
    pass