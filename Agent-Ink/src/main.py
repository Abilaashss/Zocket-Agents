from agents import *
from tasks import *
if __name__:
    planner = planner_agent()
    writer = writer_agent()
    editor = editor_agent()

    plan = plan_task()
    write = write_task()
    edit = editor_task()

    crew = Crew(
        agents = [planner, writer, editor],
        tasks = [plan, write, edit],
        process = Process.sequential,
        verbose = True
    )
    result = crew.kickoff()
    print(result)

