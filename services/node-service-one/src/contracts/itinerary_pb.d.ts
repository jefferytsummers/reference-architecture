// package: itinerary
// file: itinerary.proto

import * as jspb from "google-protobuf";

export class GetItineraryRequest extends jspb.Message {
  getItineraryId(): string;
  setItineraryId(value: string): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetItineraryRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetItineraryRequest): GetItineraryRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetItineraryRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetItineraryRequest;
  static deserializeBinaryFromReader(message: GetItineraryRequest, reader: jspb.BinaryReader): GetItineraryRequest;
}

export namespace GetItineraryRequest {
  export type AsObject = {
    itineraryId: string,
  }
}

export class GetItineraryReply extends jspb.Message {
  getDate(): string;
  setDate(value: string): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetItineraryReply.AsObject;
  static toObject(includeInstance: boolean, msg: GetItineraryReply): GetItineraryReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetItineraryReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetItineraryReply;
  static deserializeBinaryFromReader(message: GetItineraryReply, reader: jspb.BinaryReader): GetItineraryReply;
}

export namespace GetItineraryReply {
  export type AsObject = {
    date: string,
  }
}

