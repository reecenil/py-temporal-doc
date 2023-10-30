# py-temporal-doc

### Sample json structure

```
{
	"callers" {
		"Periodic": {"workflows": ["Workflow1", "Workflow2"]}
		"PostMethod": {"workflows": ["Workflow3", "Workflow4"]}
	},
	"workflows" {
		"Workflow1": {
			"child_workflows": ["ChildWorkflow1", "ChildWorkflow2"]
			"activities": ["Activity1", "Activity2"]
			"comment": "comment..."
		}
		"Workflow2": {
			"child_workflows": []
			"activities": ["Activity2", "Activity3"]
			"comment": "comment..."
		}
		"Workflow3": {
			"child_workflows": []
			"activities": ["Activity3", "Activity4"]
			"comment": "comment..."
		}
		"Workflow4": {
			"child_workflows": []
			"activities": ["Activity4"]
			"comment": "comment..."
		}
		"ChildWorkflow1": {
			"child_workflows": []
			"activities": ["Activity1"]
			"comment": "comment..."
		}
		"ChildWorkflow2": {
			"child_workflows": []
			"activities": ["Activity2"]
			"comment": "comment..."
		}
	}
	"activities" {
		"Activity1": {"comment": "comment..."}
		"Activity2": {"comment": "comment..."}
		"Activity3": {"comment": "comment..."}
		"Activity4": {"comment": "comment..."}
	}
}
```

### Decorator Usage

```
@activity.defn
async def activity1() -> None:
    pass
    
@activity.defn
async def activity2() -> None:
    pass
    
@activity.defn
async def child_activity1() -> None:
    pass
    
@activity.defn
async def child_activity2() -> None:
    pass

@document.workflow_sequence(
    child_activity1
)
@workflow.defn
class ChildWorkflow1:

    @workflow.run
    async def run(self) -> None:    
        pass
        

@document.workflow_sequence(
    child_activity2
)  
@workflow.defn
class ChildWorkflow2:

    @workflow.run
    async def run(self) -> None:    
        pass
        
        
@document.workflow_sequence( # Decorator to indicate the sequence of activities and child workflows inside a workflow
    activity1,
    ChildWorkflow1,
    activity2,
    ChildWorkflow2
)
@workflow.defn
class Workflow1:

    @workflow.run
    async def run(self) -> None:    
        pass
        

@document.workflow_sequence(
    ChildWorkflow1,
    ChildWorkflow2
)  
@workflow.defn
class Workflow2:

    @workflow.run
    async def run(self) -> None:    
        pass
       
        
@document.workflow_caller( # Decorator to indicate the starting point on when the workflows are called
    Workflow1,
)
def call_worklow1():
    client = await temporal_client(namespace=TEMPORAL_NAMESPACE)
    
    await temporal.execute_workflow(
        Workflow1.run,
        ...
    )
    
@document.workflow_caller(
    Workflow2
)
def call_worklow2():
    client = await temporal_client(namespace=TEMPORAL_NAMESPACE)
    
    await temporal.execute_workflow(
        Workflow2.run,
        ...
    )

```