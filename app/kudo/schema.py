#https://marshmallow.readthedocs.io/en/3.0/
from marshmallow import Schema, fields

#Github repository sent by clients
class GithubRepoSchema(Schema):
	id = fields.Int(required=True)
	repo_name = fields.Str()
	full_name = fields.Str()
	language = fields.Str()
	description = fields.Str()
	repo_url = fields.URL()

#Data you are going to persist in the database
class KudoSchema(GithubRepoSchema):
	user_id = fields.Email(required=True)
