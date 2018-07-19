export function renderHashtags(chain) {

    let rendered = chain.text;

    rendered = rendered.replace(/(<([^>]+)>)/ig, '');

    chain.tags
        .map(tag => new RegExp(`(#${tag})`, 'g'))
        .forEach(regex => {
            rendered = rendered.replace(regex, `<a href='#'>$1</a>`);
        });

    return Promise.resolve(rendered);

}

export function renderMentions(chain) {



}