# legend

Error: A field group must have an accessible label. Use `fieldset` and `legend`.

Error: The requested field group name is missing.

Error: `aria-labelledby` must reference one (or more) valid element `id` attributes.

Error: `for` must be an `id` reference to a form control and may not reference other element types. To create the intended relationship, the `div` must have a `role` of "group" and an `aria-labelledby` attribute that references the `label`. Or use `fieldset` and `legend`.

Error: A `label` alone cannot be used to provide an accessible label for a group of fields. Labels can only be associated with a single field using the `for` attribute. Use `fieldset` and `legend`.

Error: In order to serve as an `id`-reference for `aria-labelledby`, the `label` must have an `id` attribute, not `for`. The `for` attribute is itself an `id`-reference to an  associated form control, which is not applicable in this case.

Error: A `div` and `p` alone are insufficient for labeling a group of related fields. Use `fieldset` & `legend` or `role="group"` and `aria-labelledby` to provide the proper semantics.

Note: a `legend` automatically provides an accessible label to its `fieldset`, making the `aria-labelledby`/`id` combo redundant. Including it might result in the code becoming more fragile code over time.

Error: The `div` has an `aria-labelledby` that is self-referential. It should reference the `label` (which should be the element with an `id`).

Error: The `form` does not need to be labelled by the `legend` as the `fieldset` & `legend` combination already provides those semantics. 

# input

Error: Checkboxes in a group should use a `name` value that ends with "[]" to allow server-side code to collect the values as an array (or similar).

Error: When a checkbox is marked as `required`, it must be checked to be valid. Per the instructions, the user only needs to choose one or more, so `required` must not be used on any of the checkbox inputs.

Error: `aria-invalid="true"` is used to accessibly indicate fields that have errors.

Error: Checkbox inputs should appear before their text label.

Error: The error message indicates the radio field is required. With radio `input` elements, you can set `required` on each `input` and browsers will only require a user to choose one of them.

Error: `aria-describedby` is not needed on an individual radio field if the description applies to the group and not the individual item. Apply it to the `fieldset` instead.

Error: The prompt did not request a radio be checked by default.

Error: An `aria-checked` attribute is unnecessary on a radio input element. The built-in `checked` attribute (or lack thereof) provides the same information.

Error: If you are using a `label` with a `for` referencing the associated field, you do not need the reciprocal relationship to be established using an `id` on the `label` and `aria-labelledby` on the `input`.

Error: The `aria-label` attributes are not necessary as that information is provided by the related `label` element.

# label

Error: All form controls must have an accessible label.

Error: For broadest accessibility, implicitly associated `label` elements should also be explicitly associated with their control, using `for`.

Note: If the checkbox control is not nested in its `label`, wrapping the two elements within another element (such as a `div`) is preferable. Having a shared parent element gives designers more control over the eventual layout of the checkbox group than a `br` does.

# description

Error: `legend` should not be used for a description. It’s for a group label.

Error: Use `aria-describedby` to reference a group description.

Error: For usability, it is recommended to put the group description at the top of the component, just after the label.

Error: Inline styles are no substitute for semantics, such as `small`.

Error: `role="alert"` is not appropriate for the error in this component.

# errors

Error: Color alone should not be used to convey errors.

Error: The error text should not be hidden when the component has an error.

Error: The error message is not a live region.

# extra

Error: When your component includes a collection of radio `input` elements with the same name, the "radiogroup" `role` is unnecessary. You only need it if you are not using true form controls. The "group" `role` is sufficient.

Note: If checkbox elements are wrapped in their `label`, `br` is unnecessary.

Note: If radio inputs are wrapped in their `label`, `br` is unnecessary.

Error: The `form` element was not requested.

Error: styles were not requested.

Note: The `div` wrapper is unnecessary.

Error: A `button` is not part of this component.

Error: JavaScript is unnecessary for this component.

Error: The response should not have been in a Markdown block.