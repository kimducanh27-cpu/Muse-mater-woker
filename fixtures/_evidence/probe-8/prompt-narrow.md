Read only this part of `.agents/skills/app-flow/SKILL.md`: the bullet list under "Hashes use lowercase SHA-256 over exact on-disk bytes" that defines `previous_register_sha256`, `event_block_sha256` and `resulting_register_sha256`.

Then answer in at most 6 lines:

1. The exact byte range hashed for `event_block_sha256`.
2. Is the stored value of that field inside or outside those bytes?
3. If inside, how is the value computed without circularity?
4. Quote the exact words in the Skill that resolve it.

Do not read any other file. Do not write anything. Do not ask questions.
