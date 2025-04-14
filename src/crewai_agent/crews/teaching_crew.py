from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task


@CrewBase
class TeachingCrews():
    
    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    @agent
    def sirzia(self) -> Agent:
        return Agent (
            config = self.agents_config["sirzia"]
        )
    @task  
    def describe1(self) -> Task:
        return Task (
            config = self.tasks_config["describe1"]
        )
    @crew
    def teaching_crew(self) -> Crew:
        return Crew(
            agents=[self.sirzia()],
            tasks=[self.describe1()],
            process=Process.sequential,
            verbose=True,
        )
