export const gasAttributesMapping = {
  state: "State",
  regular: "Regular",
  premium: "Premium",
  diesel: "Diesel"
};

export interface State {
  state: string;
  regular: number;
  premium: number;
  diesel: number;
}


