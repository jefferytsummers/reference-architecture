// package: user
// file: user.proto

import * as jspb from "google-protobuf";

export class GetUserRequest extends jspb.Message {
  getUserid(): string;
  setUserid(value: string): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetUserRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetUserRequest): GetUserRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetUserRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetUserRequest;
  static deserializeBinaryFromReader(message: GetUserRequest, reader: jspb.BinaryReader): GetUserRequest;
}

export namespace GetUserRequest {
  export type AsObject = {
    userid: string,
  }
}

export class GetUserReply extends jspb.Message {
  getName(): string;
  setName(value: string): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetUserReply.AsObject;
  static toObject(includeInstance: boolean, msg: GetUserReply): GetUserReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetUserReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetUserReply;
  static deserializeBinaryFromReader(message: GetUserReply, reader: jspb.BinaryReader): GetUserReply;
}

export namespace GetUserReply {
  export type AsObject = {
    name: string,
  }
}

export class UpdateUserNameRequest extends jspb.Message {
  getUserid(): string;
  setUserid(value: string): void;

  getUpdatedname(): string;
  setUpdatedname(value: string): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UpdateUserNameRequest.AsObject;
  static toObject(includeInstance: boolean, msg: UpdateUserNameRequest): UpdateUserNameRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UpdateUserNameRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UpdateUserNameRequest;
  static deserializeBinaryFromReader(message: UpdateUserNameRequest, reader: jspb.BinaryReader): UpdateUserNameRequest;
}

export namespace UpdateUserNameRequest {
  export type AsObject = {
    userid: string,
    updatedname: string,
  }
}

export class UpdateUserNameReply extends jspb.Message {
  getSuccess(): boolean;
  setSuccess(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UpdateUserNameReply.AsObject;
  static toObject(includeInstance: boolean, msg: UpdateUserNameReply): UpdateUserNameReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UpdateUserNameReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UpdateUserNameReply;
  static deserializeBinaryFromReader(message: UpdateUserNameReply, reader: jspb.BinaryReader): UpdateUserNameReply;
}

export namespace UpdateUserNameReply {
  export type AsObject = {
    success: boolean,
  }
}

