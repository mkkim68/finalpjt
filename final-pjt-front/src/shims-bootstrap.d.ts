// src/shims-bootstrap.d.ts
declare module "bootstrap/js/dist/collapse" {
  export default class Collapse {
    constructor(element: Element, options?: any);
    static getInstance(element: Element): Collapse;
    hide(): void;
    show(): void;
    toggle(): void;
  }
}
