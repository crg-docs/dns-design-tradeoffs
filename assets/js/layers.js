(() => {
  "use strict";

  const dataElement = document.getElementById("document-layer-data");
  const content = document.querySelector(".markdown-body");
  if (!dataElement || !content) return;

  const data = JSON.parse(dataElement.textContent);
  const notes = new Map();

  function locate(entry) {
    const nodes = [];
    const walker = document.createTreeWalker(content, NodeFilter.SHOW_TEXT, {
      acceptNode: (node) => node.parentElement.closest("script, style, .document-layer-note")
        ? NodeFilter.FILTER_REJECT : NodeFilter.FILTER_ACCEPT
    });
    let text = "";
    while (walker.nextNode()) {
      nodes.push({ node: walker.currentNode, start: text.length });
      text += walker.currentNode.data;
    }
    const context = `${entry.prefix || ""}${entry.anchor}${entry.suffix || ""}`;
    const contextIndex = text.indexOf(context);
    if (contextIndex < 0 || text.indexOf(context, contextIndex + 1) >= 0) return null;
    const anchorIndex = contextIndex + (entry.prefix || "").length;
    const match = nodes.find(({ node, start }) => anchorIndex >= start && anchorIndex < start + node.data.length);
    let target = match && match.node.parentElement.closest("p, li, blockquote, table, h1, h2, h3, h4, h5, h6");
    while (target && target.parentElement !== content) target = target.parentElement;
    return target;
  }

  data.entries.forEach((entry) => {
    const target = locate(entry);
    if (!target) return;
    const note = document.createElement("aside");
    note.className = "document-layer-note";
    note.dataset.layerType = entry.type;
    note.style.setProperty("--layer-color", data.types[entry.type].color);
    note.hidden = true;
    const heading = document.createElement("strong");
    heading.textContent = data.types[entry.type].label;
    const body = document.createElement("div");
    body.textContent = entry.content;
    note.append(heading, body);
    target.insertAdjacentElement(entry.position === "before" ? "beforebegin" : "afterend", note);
    if (!notes.has(entry.type)) notes.set(entry.type, []);
    notes.get(entry.type).push(note);
  });

  const panel = document.createElement("details");
  panel.className = "layer-panel";
  panel.innerHTML = "<summary>Layer</summary>";
  const controls = document.createElement("fieldset");
  const addToggle = (label, checked, onChange) => {
    const row = document.createElement("label");
    const input = document.createElement("input");
    input.type = "checkbox";
    input.checked = checked;
    input.addEventListener("change", () => onChange(input.checked));
    row.append(input, label);
    controls.append(row);
  };
  addToggle("本文", true, (visible) => document.body.classList.toggle("layer-body-hidden", !visible));
  Object.entries(data.types).forEach(([type, definition]) => {
    addToggle(definition.label, false, (visible) => (notes.get(type) || []).forEach((note) => { note.hidden = !visible; }));
  });
  panel.append(controls);
  document.body.append(panel);
})();
