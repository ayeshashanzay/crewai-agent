from crewai.flow.flow import Flow,start,listen
from src.crewai_agent.crews.teaching_crew import TeachingCrews
from litellm import completion 
from dotenv import find_dotenv, load_dotenv


_:bool=load_dotenv(find_dotenv())

class panaFlow(Flow):

    @start()
    def genetate_topic(self):
        response = completion (
            model="gemini/gemini-1.5-flash",
            # api_key=api_key,
            messages=[{"role":"user","content":"share the most trending topic in Ai  World "}]
        )
        result = response["choices"][0]["message"]["content"]
        self.state["topic"] = result 
        print(f"Step 1 Topic: {self.state["topic"]} ")
        return result

    @listen(genetate_topic)
    def generate_content(self):
        print("Step 2 Generate Content")
        teaching_crew = TeachingCrews().teaching_crew().kickoff(
            inputs={"topic":self.state['topic']}
        )
        return {"topic":self.state.topic, "content": self.teaching_crew}

def kickoff():
    obj = panaFlow()
    result =  obj.kickoff()
    print(result)