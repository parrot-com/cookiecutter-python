from prometheus_client import Counter

PREFIX = "{{ cookiecutter.module_name }}"

TICKS = Counter(f"{PREFIX}_ticks_total", "Number of ticks")
