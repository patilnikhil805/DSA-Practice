function capitalize(paragraph) {
  // (^|(?:\.+|\?+|!+))  => start of string OR a run of '.' OR '?' OR '!'
  // (\s*)               => any spaces right after that boundary (preserve them)
  // ([a-z])             => the first lowercase letter to capitalize
  return paragraph.replace(/(^|(?:\.+|\?+|!+))(\s*)([a-z])/g,
    (_, boundary, spaces, letter) => boundary + spaces + letter.toUpperCase()
  );
}