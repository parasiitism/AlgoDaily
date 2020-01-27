const _stringToCamelCase = function(input) {
	return input
		.toLowerCase()
		.replace(/[^a-zA-Z0-9]+(.)/g, (m, character) =>
			character.toUpperCase()
		);
};

const _isObject = function(item) {
	return typeof item === "object" && !Array.isArray(item) && item !== null;
};

// recursion:
// if its an object, just camelize every key and put its value back in recursively
// if its an array, camelize every child recursively
const camelizeObject = function(obj) {
	if (_isObject(obj)) {
		const res = {};
		Object.keys(obj).forEach(key => {
			const camelKey = _stringToCamelCase(key);
			res[camelKey] = camelizeObject(obj[key]);
		});
		return res;
	} else if (Array.isArray(obj)) {
		const newItems = [];
		obj.forEach(item => {
			newItems.push(camelizeObject(item));
		});
		return newItems;
	}
	return obj;
};

// test

const input = {
	a_bc: "hi",
	ab_cd: true,
	ab_cde: 1,
	ab_cd_fg: {
		a_bc: "hi",
		ab_cd: false,
		ab_cde: 2
	},
	ab_cd_fg_hi: [
		1,
		true,
		"hi",
		{
			a_bc: "hi",
			ab_cd: true
		},
		[
			{
				ab_cd: true,
				ab_cde: 1
			},
			{
				ab_cd: true,
				ab_cde: 1
			}
		]
	]
};
console.log(camelizeObject(input));
