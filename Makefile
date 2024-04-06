SHELL := /bin/zsh

PYTHON_SERVICES := user-service itinerary-service
DOTNET_SERVICES := dotnet-service-one
NODE_SERVICES := node-service-one
PYTHON_APIS := save-the-date
DOTNET_APIS := dotnet-api-one
NODE_APIS := node-api-one

.PHONY: npm-install all python dotnet node contracts clean-contracts $(PYTHON_SERVICES) $(DOTNET_SERVICES) $(NODE_SERVICES) $(PYTHON_APIS) $(DOTNET_APIS) $(NODE_APIS)

python: $(PYTHON_SERVICES) $(PYTHON_APIS)

dotnet: $(DOTNET_SERVICES) $(DOTNET_APIS)

node: $(NODE_SERVICES) $(NODE_APIS)

contracts: python dotnet node

queue:
	@echo "Generating Python code for Command Queue..."
	python -m grpc_tools.protoc --proto_path=contracts/ --python_out=command-queue/back-tier/src/contracts --grpc_python_out=command-queue/back-tier/src/contracts contracts/*.proto
	@echo "Python code generated successfully for $@."

$(PYTHON_SERVICES):
	@echo "Generating Python code for $@..."
	python -m grpc_tools.protoc --proto_path=contracts/ --python_out=./services/$@/contracts --grpc_python_out=./services/$@/contracts contracts/*.proto
	@echo "Python code generated successfully for $@."

$(DOTNET_SERVICES):
	@echo "Generating C# code for $@..."
	protoc --proto_path=contracts/ --csharp_out=services/$@/contracts contracts/*.proto
	@echo "C# code generated successfully for $@."

$(NODE_SERVICES):
	@echo "Generating TypeScript code for $@..."
	protoc --proto_path=contracts/ --ts_out=services/$@/src/contracts --ts_opt=generate_package_definition contracts/*.proto
	@echo "TypeScript code generated successfully for $@."
	@echo "Compiling TypeScript code for $@..."
	cd services/$@; npm run build
	@echo "TypeScript code compiled successfully for $@."

$(PYTHON_APIS):
	@echo "Generating Python code for $@..."
	protoc --proto_path=contracts/ --python_out=orchestration/$@/contracts contracts/*.proto
	@echo "Python code generated successfully for $@."

$(DOTNET_APIS):
	@echo "Generating C# code for $@..."
	protoc --proto_path=contracts/ --csharp_out=orchestration/$@/contracts contracts/*.proto
	@echo "C# code generated successfully for $@."

$(NODE_APIS):
	@echo "Generating TypeScript code for $@..."
	protoc --proto_path=contracts/ --ts_out=orchestration/$@/src/contracts --ts_opt=generate_package_definition contracts/*.proto
	@echo "TypeScript code generated successfully for $@."
	@echo "Compiling TypeScript code for $@..."
	cd orchestration/$@; npm run build
	@echo "TypeScript code compiled successfully for $@."

clean-contracts:
	@echo "Cleaning generated files..."
	find $(addsuffix /src/contracts, command-queue/back-tier) -type f -delete
	find $(addsuffix /contracts/, $(addprefix services/, $(PYTHON_SERVICES) $(DOTNET_SERVICES))) -type f -delete
	find $(addsuffix /src/contracts/, $(addprefix services/, $(NODE_SERVICES))) -type f -delete
	find $(addsuffix /contracts/, $(addprefix orchestration/, $(PYTHON_APIS) $(DOTNET_APIS))) -type f -delete
	find $(addsuffix /src/contracts/, $(addprefix orchestration/, $(NODE_APIS))) -type f -delete
	@echo "Cleanup completed."

npm-install:
	source ~/.nvm/nvm.sh && nvm use && npm install