/* 
  Given an array of strings
  return a sum to represent how many times each array item is found (a frequency table)
  Useful methods:
    Object.hasOwnProperty("keyName")
      - returns true or false if the object has the key or not
    Python: key in dict
*/

const arr1 = ["a", "a", "a"];
const expected1 = {
  a: 3,
};

const arr2 = ["a", "b", "a", "c", "B", "c", "c", "d"];
const expected2 = {
  a: 2,
  b: 1,
  c: 3,
  B: 1,
  d: 1,
};

const arr3 = [];
const expected3 = {};

/**
 * Builds a frequency table based on the given array.
 * - Time: O(?).
 * - Space: O(?).
 * @param {Array<string>} arr
 * @return {Object<string, number>} A frequency table where the keys are items
 *    from the given arr and the values are the amnt of times that item occurs.
 */
 function frequencyTableBuilder(arr) {
  const freqTable = {};

  for (let i = 0; i < arr.length; i++) {
    const str = arr[i];

    if (freqTable.hasOwnProperty(str) === false) {
      // first occurrence found
      freqTable[str] = 1;
    } else {
      freqTable[str]++;
    }
  }
  return freqTable;
}

function frequencyTableBuilder2(arr) {
  const freqTable = {};

  for (const str of arr) {
    if (freqTable.hasOwnProperty(str) === false) {
      // first occurrence found
      freqTable[str] = 1;
    } else {
      freqTable[str]++;
    }
  }

  return freqTable;
}

module.exports = { frequencyTableBuilder };

/*****************************************************************************/
// BONUS!!!!!
  
/* 
  Reverse Word Order
  Given a string of words (with spaces)
  return a new string with words in reverse sequence.
*/

const str1 = "This is a test";
const expected1 = "test a is This";

/**
 * Reverses the order of the words but not the words themselves form the given
 * string of space separated words.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} wordsStr A string containing space separated words.
 * @return {string} The given string with the word order reversed but the words
 *    themselves are not reversed.
 */

//  1. split string to array
//  2. reverse array - loop across array and change index of each item
//  3. push each item in array to a new string, separated by space

function reverseWordOrder(wordsStr) {
  // if all spaces
  if (wordsStr == false) {
    return wordsStr;
  }

  let currWord = "";
  let reversedWordOrder = "";

  for (let i = wordsStr.length - 1; i >= 0; --i) {
    if (wordsStr[i] !== " ") {
      // prepend so the Word itself is not reversed by looping backWords
      currWord = wordsStr[i] + currWord;
    }
    // space found
    else {
      // add a space in front of the word, except on first word
      if (reversedWordOrder.length > 0) {
        currWord = " " + currWord;
      }

      reversedWordOrder += currWord;
      currWord = "";
    }
  }

  // no space at end of string means we didn't add the last word
  if (currWord.length > 0) {
    reversedWordOrder += " " + currWord;
  }
  return reversedWordOrder;
}


module.exports = { reverseWordOrder };

/*****************************************************************************/