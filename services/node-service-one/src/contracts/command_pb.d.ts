// package: commandqueue
// file: command.proto

import * as jspb from "google-protobuf";

export class Command extends jspb.Message {
  getCommandId(): string;
  setCommandId(value: string): void;

  getServiceName(): string;
  setServiceName(value: string): void;

  getCommandType(): string;
  setCommandType(value: string): void;

  getPayload(): Uint8Array | string;
  getPayload_asU8(): Uint8Array;
  getPayload_asB64(): string;
  setPayload(value: Uint8Array | string): void;

  getPriority(): number;
  setPriority(value: number): void;

  getRetryCount(): number;
  setRetryCount(value: number): void;

  getCreatedAt(): string;
  setCreatedAt(value: string): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): Command.AsObject;
  static toObject(includeInstance: boolean, msg: Command): Command.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: Command, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): Command;
  static deserializeBinaryFromReader(message: Command, reader: jspb.BinaryReader): Command;
}

export namespace Command {
  export type AsObject = {
    commandId: string,
    serviceName: string,
    commandType: string,
    payload: Uint8Array | string,
    priority: number,
    retryCount: number,
    createdAt: string,
  }
}

export class EnqueueCommandRequest extends jspb.Message {
  hasCommand(): boolean;
  clearCommand(): void;
  getCommand(): Command | undefined;
  setCommand(value?: Command): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): EnqueueCommandRequest.AsObject;
  static toObject(includeInstance: boolean, msg: EnqueueCommandRequest): EnqueueCommandRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: EnqueueCommandRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): EnqueueCommandRequest;
  static deserializeBinaryFromReader(message: EnqueueCommandRequest, reader: jspb.BinaryReader): EnqueueCommandRequest;
}

export namespace EnqueueCommandRequest {
  export type AsObject = {
    command?: Command.AsObject,
  }
}

export class EnqueueCommandResponse extends jspb.Message {
  getSuccess(): boolean;
  setSuccess(value: boolean): void;

  getMessage(): string;
  setMessage(value: string): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): EnqueueCommandResponse.AsObject;
  static toObject(includeInstance: boolean, msg: EnqueueCommandResponse): EnqueueCommandResponse.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: EnqueueCommandResponse, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): EnqueueCommandResponse;
  static deserializeBinaryFromReader(message: EnqueueCommandResponse, reader: jspb.BinaryReader): EnqueueCommandResponse;
}

export namespace EnqueueCommandResponse {
  export type AsObject = {
    success: boolean,
    message: string,
  }
}

export class DequeueCommandRequest extends jspb.Message {
  getServiceName(): string;
  setServiceName(value: string): void;

  getCommandId(): string;
  setCommandId(value: string): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): DequeueCommandRequest.AsObject;
  static toObject(includeInstance: boolean, msg: DequeueCommandRequest): DequeueCommandRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: DequeueCommandRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): DequeueCommandRequest;
  static deserializeBinaryFromReader(message: DequeueCommandRequest, reader: jspb.BinaryReader): DequeueCommandRequest;
}

export namespace DequeueCommandRequest {
  export type AsObject = {
    serviceName: string,
    commandId: string,
  }
}

export class DequeueCommandResponse extends jspb.Message {
  hasCommand(): boolean;
  clearCommand(): void;
  getCommand(): Command | undefined;
  setCommand(value?: Command): void;

  getSuccess(): boolean;
  setSuccess(value: boolean): void;

  getMessage(): string;
  setMessage(value: string): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): DequeueCommandResponse.AsObject;
  static toObject(includeInstance: boolean, msg: DequeueCommandResponse): DequeueCommandResponse.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: DequeueCommandResponse, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): DequeueCommandResponse;
  static deserializeBinaryFromReader(message: DequeueCommandResponse, reader: jspb.BinaryReader): DequeueCommandResponse;
}

export namespace DequeueCommandResponse {
  export type AsObject = {
    command?: Command.AsObject,
    success: boolean,
    message: string,
  }
}

export class RetryCommandRequest extends jspb.Message {
  getCommandId(): string;
  setCommandId(value: string): void;

  getServiceName(): string;
  setServiceName(value: string): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): RetryCommandRequest.AsObject;
  static toObject(includeInstance: boolean, msg: RetryCommandRequest): RetryCommandRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: RetryCommandRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): RetryCommandRequest;
  static deserializeBinaryFromReader(message: RetryCommandRequest, reader: jspb.BinaryReader): RetryCommandRequest;
}

export namespace RetryCommandRequest {
  export type AsObject = {
    commandId: string,
    serviceName: string,
  }
}

export class RetryCommandResponse extends jspb.Message {
  getSuccess(): boolean;
  setSuccess(value: boolean): void;

  getMessage(): string;
  setMessage(value: string): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): RetryCommandResponse.AsObject;
  static toObject(includeInstance: boolean, msg: RetryCommandResponse): RetryCommandResponse.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: RetryCommandResponse, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): RetryCommandResponse;
  static deserializeBinaryFromReader(message: RetryCommandResponse, reader: jspb.BinaryReader): RetryCommandResponse;
}

export namespace RetryCommandResponse {
  export type AsObject = {
    success: boolean,
    message: string,
  }
}

export class LogQueueStateRequest extends jspb.Message {
  getServiceName(): string;
  setServiceName(value: string): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): LogQueueStateRequest.AsObject;
  static toObject(includeInstance: boolean, msg: LogQueueStateRequest): LogQueueStateRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: LogQueueStateRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): LogQueueStateRequest;
  static deserializeBinaryFromReader(message: LogQueueStateRequest, reader: jspb.BinaryReader): LogQueueStateRequest;
}

export namespace LogQueueStateRequest {
  export type AsObject = {
    serviceName: string,
  }
}

export class LogQueueStateResponse extends jspb.Message {
  getCommandCount(): number;
  setCommandCount(value: number): void;

  getProcessing(): boolean;
  setProcessing(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): LogQueueStateResponse.AsObject;
  static toObject(includeInstance: boolean, msg: LogQueueStateResponse): LogQueueStateResponse.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: LogQueueStateResponse, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): LogQueueStateResponse;
  static deserializeBinaryFromReader(message: LogQueueStateResponse, reader: jspb.BinaryReader): LogQueueStateResponse;
}

export namespace LogQueueStateResponse {
  export type AsObject = {
    commandCount: number,
    processing: boolean,
  }
}

