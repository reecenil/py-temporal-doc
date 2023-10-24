# py-temporal-doc

Sample json structure

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