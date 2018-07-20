export function render(chain) {
    return Promise.resolve(chain)
        .then(removeHtmlTags)
        .then(renderTags)
        .then(renderMentions)
        .then(renderStrong)
        .then(renderLinebreak);
}

export function removeHtmlTags(chain) {

    return new Promise((resolve, reject) => {

        let {
            text
        } = chain;

        text = text.replace(/<([^>]+)>/ig, '&lt;$1&gt;');

        const result = { ...chain,
            text
        };

        return resolve(result);

    });

}

export function renderTags(chain) {

    return new Promise((resolve, reject) => {

        let {
            tags,
            text
        } = chain;

        for (const t of tags) {
            const regex = new RegExp(`(#${t.name})`, 'g');
            text = text.replace(regex, `<a href='#${t.id}'>$1</a>`);
        }

        const result = { ...chain,
            text
        };

        return resolve(result);

    });

}

export function renderMentions(chain) {

    return new Promise((resolve, reject) => {

        let {
            mentions,
            text
        } = chain;

        for (const m of mentions) {
            const regex = new RegExp(`(@${m.user.username})`, 'g');
            text = text.replace(regex, `<a href='#${m.id}'>$1</a>`);
        }

        const result = { ...chain,
            text
        };

        return resolve(result);

    });

}

export function renderStrong(chain) {

    return new Promise((resolve, reject) => {

        let {
            text
        } = chain;

        text = text.replace(/\*\*(.+?)\*\*/ig, '<strong>$1</strong>');

        const result = { ...chain,
            text
        };

        return resolve(result);

    });

}

export function renderLinebreak(chain) {

    return new Promise((resolve, reject) => {

        let {
            text
        } = chain;

        text = text.replace(/\n/g, '<br>');

        const result = { ...chain,
            text
        };

        return resolve(result);

    });

}