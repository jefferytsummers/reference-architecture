```
>.  src/

		command-queue/
			producers[] // Send messages to consumers
			consumers[] // Publish messages to producers
			/enqueue // add messages to the queue
			/dequeue // remove messages from the queue
			/requeue // move a message to the end of the queue
			
	  orchestration-tier/
		  api_one/ // Command orchestrator
			  src/
				  entities/ // Display aggregation/business logic
				  producer.[ts, py, cs, go, etc.] // Send a message to the queue
				  contracts/
					  contract_one.[ts, py, cs, go, etc.]
					  ...
			...
		service-tier/
			service_one/ // Microservice
				src/
					consumer.[ts, py, cs, go, etc.]
					contract.[ts, py, cs, go, etc.]
			...
		contracts/
			entity_one.proto // api contracts
			...
		generated/
			contract.[ts, py, cs, go, etc.]
		Makefile	// Glue it all together
		
		< -- Other stuff -- >
		dotnet_proto_tools/ # dotnet console app for code gen
		Pipfile       // python code gen 
		Pipfile.lock. //
		// ... the rest of the languages
		
```
