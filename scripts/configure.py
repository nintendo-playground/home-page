
import secrets

env = {
	"COMPOSE_PROJECT_NAME": input("Project name: "),
	"PORT": input("Port: "),
	
	"SECRET_KEY": secrets.token_hex(16)
}

env = "".join("%s=%s\n" %(key, value) for key, value in env.items())

with open(".env", "w") as f:
	f.write(env)
