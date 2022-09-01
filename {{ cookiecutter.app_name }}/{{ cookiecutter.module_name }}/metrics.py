from prometheus_client import Counter

PREFIX = "{{ cookiecutter.app_name }}"

TICKS = Counter(f"{PREFIX}_ticks_total", "Number of ticks")
