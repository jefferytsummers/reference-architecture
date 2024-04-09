SHELL := /bin/zsh

PYTHON_SERVICES := user-service itinerary-service
DOTNET_SERVICES := dotnet-service-one
NODE_SERVICES := node-service-one

PYTHON_APIS := save-the-date
DOTNET_APIS := dotnet-api-one
NODE_APIS := node-api-one

YELLOW := \033[0;33m
GREEN := \033[0;32m
RED := \033[0;31m
ORANGE := \033[0;38;5;208m
NC := \033[0m

.PHONY: npm-install all python dotnet node contracts clean-contracts $(PYTHON_SERVICES) $(DOTNET_SERVICES) $(NODE_SERVICES) $(PYTHON_APIS) $(DOTNET_APIS) $(NODE_APIS)

python: $(PYTHON_SERVICES) $(PYTHON_APIS)
dotnet: $(DOTNET_SERVICES) $(DOTNET_APIS)
node: $(NODE_SERVICES) $(NODE_APIS)

contracts: python dotnet node

queue:
	@echo "${ORANGE}Generating Python code for Command Queue...${NC}"
	@python -m grpc_tools.protoc -I contracts/ --python_out=command-queue/back-tier/src/contracts/ --grpc_python_out=command-queue/back-tier/src/contracts/ contracts/command.proto || (echo "${RED}Failed to generate Python code for Command Queue.${NC}" && exit 1)
	@echo "${GREEN}Python code generated successfully for $@.${NC}"

$(PYTHON_SERVICES):
	@echo "${ORANGE}Generating Python code for $@...${NC}"
	@python -m grpc_tools.protoc --proto_path=contracts/ --python_out=./services/$@/src/contracts --grpc_python_out=./services/$@/src/contracts contracts/*.proto || (echo "${RED}Failed to generate Python code for $@.${NC}" && exit 1)
	@echo "${GREEN}Python code generated successfully for $@.${NC}"

$(DOTNET_SERVICES):
	@echo "${ORANGE}Generating C# code for $@...${NC}"
	@protoc --proto_path=contracts/ --csharp_out=services/$@/contracts contracts/*.proto || (echo "${RED}Failed to generate C# code for $@.${NC}" && exit 1)
	@echo "${GREEN}C# code generated successfully for $@.${NC}"

$(NODE_SERVICES):
	@echo "${ORANGE}Generating TypeScript code for $@...${NC}"
	@protoc --proto_path=contracts/ --ts_out=services/$@/src/contracts --ts_opt=generate_package_definition contracts/*.proto || (echo "${RED}Failed to generate TypeScript code for $@.${NC}" && exit 1)
	@echo "${GREEN}TypeScript code generated successfully for $@.${NC}"
	@echo "${ORANGE}Compiling TypeScript code for $@...${NC}"
	@cd services/$@; npm run build || (echo "${RED}Failed to compile TypeScript code for $@.${NC}" && exit 1)
	@echo "${GREEN}TypeScript code compiled successfully for $@.${NC}"

$(PYTHON_APIS):
	@echo "${ORANGE}Generating Python code for $@...${NC}"
	@protoc --proto_path=contracts/ --python_out=orchestration/$@/contracts contracts/*.proto || (echo "${RED}Failed to generate Python code for $@.${NC}" && exit 1)
	@echo "${GREEN}Python code generated successfully for $@.${NC}"

$(DOTNET_APIS):
	@echo "${ORANGE}Generating C# code for $@...${NC}"
	@protoc --proto_path=contracts/ --csharp_out=orchestration/$@/contracts contracts/*.proto || (echo "${RED}Failed to generate C# code for $@.${NC}" && exit 1)
	@echo "${GREEN}C# code generated successfully for $@.${NC}"

$(NODE_APIS):
	@echo "${ORANGE}Generating TypeScript code for $@...${NC}"
	@protoc --proto_path=contracts/ --ts_out=orchestration/$@/src/contracts --ts_opt=generate_package_definition contracts/*.proto || (echo "${RED}Failed to generate TypeScript code for $@.${NC}" && exit 1)
	@echo "${GREEN}TypeScript code generated successfully for $@.${NC}"
	@echo "${ORANGE}Compiling TypeScript code for $@...${NC}"
	@cd orchestration/$@; npm run build || (echo "${RED}Failed to compile TypeScript code for $@.${NC}" && exit 1)
	@echo "${GREEN}TypeScript code compiled successfully for $@.${NC}"

clean-contracts:
	@echo "${ORANGE}Cleaning generated files...${NC}"
	@find $(addsuffix /src/contracts, command-queue/back-tier) -type f ! -name "__init__.py" -delete || (echo "${RED}Failed to clean generated files.${NC}" && exit )
	@find $(addsuffix /src/contracts/, $(addprefix services/, $(PYTHON_SERVICES) $(DOTNET_SERVICES))) -type f -delete || (echo "${RED}Failed to clean generated files.${NC}" && exit 1)
	@find $(addsuffix /src/contracts/, $(addprefix services/, $(NODE_SERVICES))) -type f -delete || (echo "${RED}Failed to clean generated files.${NC}" && exit 1)
	@find $(addsuffix /src/contracts/, $(addprefix orchestration/, $(PYTHON_APIS) $(DOTNET_APIS))) -type f -delete || (echo "${RED}Failed to clean generated files.${NC}" && exit 1)
	@find $(addsuffix /src/contracts/, $(addprefix orchestration/, $(NODE_APIS))) -type f -delete || (echo "${RED}Failed to clean generated files.${NC}" && exit 1)
	@echo "${GREEN}Cleanup completed.${NC}"

npm-install:
	@source ~/.nvm/nvm.sh && nvm use && npm install || (echo "${RED}Failed to run npm install.${NC}" && exit 1)