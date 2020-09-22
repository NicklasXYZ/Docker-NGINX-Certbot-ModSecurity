
#------------------------------------------------------------------------------#
#                     Author     : Nicklas Sindlev Andersen                    #
#------------------------------------------------------------------------------#
# File description: ...
#------------------------------------------------------------------------------#
#               Import packages from the python standard library               #
#------------------------------------------------------------------------------#
import os
import argparse
import json
#------------------------------------------------------------------------------#
#                             Import thrid party packages                      #
#------------------------------------------------------------------------------#
from environs import Env
import jinja2

# Parse commadnline arguments
#----------------------------------------------------------------------#
def parse_commandline_args(args_list = None):
    """ Setup, parse and validate given commandline arguments.
    """
    # Create main parser
    parser = argparse.ArgumentParser(description = "")
    add_parser_arguments(parser)
    # Parse commandline arguments
    args = parser.parse_args(args_list)
    return args

def add_required_parser_arguments(parser):
    """
    """
    parser.add_argument("-env_file", "--env_file",
        required = True,
        default = ".env",
        type = str,
        help = "Specify the name of the environment variable file."
    )

def add_parser_arguments(parser):
    """ 
    """
    # Add required commandline arguments:
    add_required_parser_arguments(parser)

# Parse file containing enviroment variables
#----------------------------------------------------------------------#
def parse_env_vars():
    """
    """
    env = Env()
    try:
        env.read_env(args.env_file, recurse = False)
    except IOError as e:
        print("INFO : File ", args.env_file, " not accessible!")
        print("Error: ", e)
    return os.environ.copy()

# Load folder containing jinja templates and generate templates according to 
# enviroment variables defined in the provided "settings.env" file
#------------------------------------------------------------------------------#
def load_jinja_templates(env_vars):
    """
    """
    jinja_templates = None
    try:
        jinja_templates = jinja2.Environment(
            autoescape = False,
            loader = jinja2.FileSystemLoader(
                searchpath = os.path.join(env_vars["TEMPLATE_DIR"]),
            ),
        )
    except KeyError as e:
        print("INFO : Enviroment variable \"TEMPLATE_DIR\" not defined!")
        print("Error: ", e)
    return jinja_templates

def render_template(jinja_templates, template_vars, template_name, outfile):
    """
    """
    # Generate configuration and other files according to the given templates
    template = jinja_templates.select_template([template_name])
    with open(outfile, "w") as file:
        print(template.render(**template_vars), file = file)

def render_templates(jinja_templates, other_vars, env_vars, prefix = ""):
    """
    """
    env_vars.update(other_vars)
    try:
        env_vars["NGINX_SERVER_NAMES"] = json.loads(env_vars["NGINX_SERVER_NAMES"])
    except KeyError as e:
        print("INFO : Enviroment variable \"NGINX_SERVER_NAMES\" not defined properly!")
        print("Error: ", e)
    try:
        env_vars["NGINX_TRUSTED_ORIGINS"] = json.loads(env_vars["NGINX_TRUSTED_ORIGINS"])
    except KeyError as e:
        print("INFO : Enviroment variable \"NGINX_TRUSTED_ORIGINS\" not defined properly!")
        print("Error: ", e)
    # Render nginx-certbot dockerfile
    render_template(
        jinja_templates,
        env_vars,
        # The template file to use. Should not be changed:
        "nginx_dockerfile.jinja",
        # Specify the correct directory to place configuration file in
        "nginx/Dockerfile", 
    )
    # Render nginx configuration file
    render_template(
        jinja_templates,
        env_vars,
        # The template file to use. Should not be changed:
        "nginx.conf.jinja",
        # Specify the correct directory to place configuration file in:
        "nginx/conf.d/nginx.conf"
    )
    # Render the main docker compose file for deploying the backend
    render_template(
        jinja_templates,
        env_vars,
        # The template file to use. Should not be changed:
        "docker-compose.yml.jinja",
        # Specify the correct directory to place configuration file in
        "docker-compose.yml", 
    )

# Generate directories based on the defined enviroment variables
#------------------------------------------------------------------------------#
def generate_directories(args, other_vars, env_vars):
    """
    """
    dir_list = []
    # # Create required output directories if they're missing
    # for dir in dir_list:
    #     if not os.path.exists(dir):
    #         os.makedirs(dir, exist_ok = True)

# Main function call...
#------------------------------------------------------------------------------#
def main(args, other_vars):
    """
    """
    # Parse file containing environment variables to be defined and used
    env_vars = parse_env_vars()
    # generate_directories(args, other_vars, env_vars)
    jinja_templates = load_jinja_templates(env_vars)
    # render_templates(jinja_templates, other_vars, env_vars, prefix = "testing")
    render_templates(jinja_templates, other_vars, env_vars, prefix = "")

#----------------------------------------------------------------------#
if __name__ == "__main__":
    """
    Script entry point...
    """
    args = parse_commandline_args()
    # Other filesnames, configs, etc.
    other_vars = {}
    main(args, other_vars)