from agents import *

def plan_task():
    plan = Task(
        description=(
            "1. Prioritise the latest trends, key players, "
            "and noteworthy news on Artifical Intelligence.\n"
            "2. Identify the target audience, considering "
            "their interests and pain points. \n"
            "3. Develop a detailed content outline including "
            "an introduction, key points, and a call to action \n"
            "4. Include SEO Keywords and relevant data or sources"
        ),
        expected_output = "A detailed content plan document "
                          "with an outline, audience analysis "
                          "SEO Keywords, and resources"  ,
        agent = planner_agent()
    )

    return plan

def write_task():
    write = Task(
    description=(
        "1. Use the content plan to craft a compelling "
            "blog post on Artificial Intelligence.\n"
        "2. Incorporate SEO keywords naturally.\n"
		"3. Sections/Subtitles are properly named "
            "in an engaging manner.\n"
        "4. Ensure the post is structured with an "
            "engaging introduction, insightful body, "
            "and a summarizing conclusion.\n"
        "5. Proofread for grammatical errors and "
            "alignment with the brand's voice.\n"
    ),
    expected_output="A well-written blog post "
        "in markdown format, ready for publication, "
        "each section should have 2 or 3 paragraphs.",
    agent=writer_agent()
)
    return write


def editor_task():
    edit = Task(
    description=("Proofread the given blog post for "
                 "grammatical errors and "
                 "alignment with the brand's voice."),
    expected_output="A well-written blog post in markdown format, "
                    "ready for publication, "
                    "each section should have 2 or 3 paragraphs.",
    agent=editor_agent()
)
    return edit
