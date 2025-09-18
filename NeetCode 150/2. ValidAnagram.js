// /**
//  * @param {string} s
//  * @param {string} t
//  * @return {boolean}
//  */
// var isAnagram = function(s, t) {
//   if (s.length !== t.length) return false;

//   const base = 'a'.charCodeAt(0);
//   const freq = new Array(26).fill(0);

//   // increment for s, decrement for t in one pass
//   for (let i = 0; i < s.length; i++) {
//     freq[s.charCodeAt(i) - base]++;
//     freq[t.charCodeAt(i) - base]--;
//   }

//   // all zeros => same multiset of letters
//   for (const count of freq) {
//     if (count !== 0) return false;
//   }
//   return true;
// };