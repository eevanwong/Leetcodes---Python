// HARD MISUNDERSTOOD Q ORIGINALLY, OVER COMPLICATEAD IT ALL 
// function firstDuplicate(a) {
//     const obj = {};
//     const arr = [];
//     for (let i = 0; i < a.length; i++) {
//         if (arr.includes(a[i])) {
//             if (obj[a[i]] == false || obj[a[i]] > i) {
//                 obj[a[i]] = i;
//             }
//         } else {
//             arr.push(a[i]);
//             obj[a[i]] = false; // [2, 1, 3, 5] {2:5, 1:-1,3:4, 5:-1}
//         }
//     }
//     let mostRecentPointer;
//     let noDuplicate = true;
//     for (let i = 0; i < arr.length; i++) {
//         if (obj[arr[i]] != false) {
//             if (mostRecentPointer !== undefined && obj[arr[i]] < obj[arr[mostRecentPointer]]) {
//                 mostRecentPointer = i
//             } else if (mostRecentPointer === undefined) {
//                 mostRecentPointer = i;
//             }
//             noDuplicate = false;
//         }
//     }
//     if (noDuplicate) {
//         return -1;
//     } else {
//         return arr[mostRecentPointer];
//     }   
// }
// unfortunately did not pass all test cases

// this game worked
function firstDuplicate(a) {
    const obj = {};
    for (const i of a) {
        if (i in obj) {
            return i;
        } else {
            obj[i] = 0;
        }
    }
    return -1;
}