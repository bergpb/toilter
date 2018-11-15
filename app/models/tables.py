from app import db

# db.Model, classe do sqlalchemy que traz o modelo de tabela padrao
class User(db.Model):
    __tablename__ = "users"
    
    __tablename__ = "users"
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), unique=True)
    password = db.Column(db.String(30), unique=True)
    name = db.Column(db.String)
    email = db.Column(db.String, unique=True)
    
    # contrutor,  obrigatoriamente quando um novo usuario for criado
    # deve ter todos esses atributos
    def __init__ (self, username, password, name, email):
        self.username = username
        self.password = password
        self.name = name
        self.email = email
        
    # representation (represenacao bonitinha de mostrar os registros salvos no banco)
    def __repr__(self):
        return "<User %r>" % self.username
    
class Post(db.Model):
    __tablename__ = "posts"
    
    id = db.Column(db.Integer, primary_key=True)
    # formato texto para que as tags html nao sejam contadas (caso as mesmas forem inseridas)
    content = db.Column(db.Text)
    # referencia o id de um usuario
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    # quando pesquisar o post,  deve trazer a info do usuario atraves do user_id
    user = db.relationship('User', foreign_keys=user_id)
    
    
    # contrutor,  obrigatoriamente quando um novo usuario for criado
    # deve ter todos esses atributos
    def __init__ (self, content, user_id):
        self.content = content
        self.user_id = user_id
        
    # representation (represenacao bonitinha de mostrar os registros salvos no banco)
    def __repr__(self):
        return "<Post %r>" % self.id


class Follow(db.Model):
    __tablename__ = "follow"
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    follower_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    user = db.relationship('User', foreign_keys=user_id)
    follower = db.relationship('User', foreign_keys=follower_id)
    