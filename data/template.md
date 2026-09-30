# Template Fields

- `id`: Question number.
- `instruction`: Full instruction text as printed on the paper for this question.
- `passage`: Reading passage or shared text for this question, or null if none. Duplicated per question, plain text with furigana removed. Notes (注) are appended at the end with a newline.
- `stem`: Question sentence as printed, plain text with no custom markup. Blank is written as `(....)`. Star position is written as `(⭐)`.
- `target`: Underlined word or phrase being asked about, or null if none. Plain text, stored separately so stem stays markup-free.
- `options`: Array of 4 answer choices as printed, plain text, in original order.
- `answer`: Correct choice number from 1 to 4.
- `correctOrder`: Full correct word order as an array (e.g. `[3,2,1,4]`) for star-ordering questions, or null otherwise.

**Note**: This template doesn't use listening sessions.
