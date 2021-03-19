/* 
  Acronyms

  Create a function that, given a string, returns the string’s acronym 
  (first letter of each word capitalized). 

  Do it with .split first if you need to, then try to do it without
*/

// 1. create a function that accepts a string
// 1a. create some variables (newString)
// 2. use the .split method to split up the words. (look this up cause idk)
// 3. figure out how to get first letter of each word.
// 4. capitalize each letter and add to new string
// 5. return the news string.

const str1 = " there's no free lunch - gotta pay yer way. ";
const expected1 = "TNFL-GPYW";

const str2 = "Live from New York, it's Saturday Night!";
const expected2 = "LFNYISN";

/**
 * Turns the given str into an acronym.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str A string to be turned into an acronym.
 * @return {string} The given str converted into an acronym.
 */
 function acronymizeWithSplit(wordsStr) {
  let acronym = "";
  const wordsArr = wordsStr.split(" ");

  for (const word of wordsArr) {
    acronym += word[0].toUpperCase();
  }
  return acronym;
}

function acronymize(wordsStr) {
  let acronym = "";
  const len = wordsStr.length;

for (let i = 0; i < len; i++) {
    while (wordsStr[i] === " " && i < len) {
      i++; // skip spaces, handles multiple spaces
    }
    // upperCase it now while we are already looping
    // to avoid upperCase having to loop over our output to upperCase
    acronym += wordsStr[i].toUpperCase();

    while (wordsStr[i] !== " " && i < len) {
      i++; // skip rest of word
    }
  }
  return acronym;
}

module.exports = { acronymize };


//************************************************************** */


/* 
  String: Reverse

  Given a string,
  return a new string that is the given string reversed
*/

const str1 = "creature";
const expected1 = "erutaerc";

const str2 = "dog";
const expected2 = "god";

/**
 * Reverses the given str.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str String to be reversed.
 * @return {string} The given str reversed.
 */
 function reverseString(str) {
  let reversed = "";

  for (let i = str.length - 1; i >= 0; i--) {
    reversed += str[i];
  }

  return reversed;
}

module.exports = { reverseString };