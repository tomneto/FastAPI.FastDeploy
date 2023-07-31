import re

from pydantic import BaseModel, validator, Field
from fastapi.param_functions import Query
from fastapi import Response, Request, Header, Depends
from typing import Optional, Union, Any, Annotated

from pydantic.fields import ModelField

from api.controllers.user import check_username, check_mail
from api.docs.rules import password_rule, username_rule, password_rule_length, username_rule_length, already_taken
from api.router.public.access.models.obj import auth as auth
from api.router.public.access.models.obj import login as login

