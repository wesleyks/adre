export type Tag = string[];
export type RawTag = string;

export interface ADR {
  id: number;
  title: string;
  date: string;
  tags: Tag[];
  content: string;
}

export interface RawADR {
  id: number;
  title: string;
  date: string;
  tags: RawTag[];
  content: string;
}
