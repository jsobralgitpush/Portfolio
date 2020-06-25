from api.models import User, Agent, Event, Group
from django.db import models
from datetime import datetime, timedelta

def get_active_users() -> User:
    """Traga todos os usuarios ativos, seu último login deve ser menor que 10 dias """
    today = datetime.today()
    queryset = User.objects.filter(last_login__gt=today - timedelta(days=10))

    return queryset



def get_amount_users() -> User:
    """Retorne a quantidade total de usuarios do sistema """
    length = len(User.objects.all())
    return length


def get_admin_users() -> User:
    """Traga todos os usuarios com grupo = 'admin"""
    queryset = User.objects.filter(group__name='admin')
    return queryset



def get_all_debug_events() -> Event:
    """Traga todos os eventos com tipo debug"""
    queryset = Event.objects.filter(level='debug')
    return queryset


def get_all_critical_events_by_user(agent) -> Event:
    """Traga todos os eventos do tipo critico de um usuário específico"""
    queryset = Event.objects.filter(level='critical',agent__name=agent)
    return queryset


def get_all_agents_by_user(username) -> Agent:
    """Traga todos os agentes de associados a um usuário pelo nome do usuário"""
    queryset = Agent.objects.filter(user__name=username)
    return queryset


def get_all_events_by_group() -> Group:
    """Traga todos os grupos que contenham alguem que possua um agente que possuem eventos do tipo information"""
    all_agents = Event.objects.filter(level='information').values_list('agent_id')
    all_users = Agent.objects.filter(id__contains=all_agents).values_list('user_id')
    all_groups = User.objects.filter(id__contains=all_users).values_list('group')
    queryset = Group.objects.filter(id__contains=all_groups)

    return queryset


