import React from 'react';
import reqwest from 'reqwest';

class SubmitGet extends React.Component {
    constructor(props) {
        super(props);

        this.state = {
            display: true
        };
    }

    submitRequest() {
        this.setState({ display: false });

        reqwest({
            url: '/get/',
            headers: {'X-Auth-Token': '88d72110d6c27f7d231c4c3197364ef0a17551c5'},
        }).then(data => {
            if (data['success']) {
                this.props.callback(data['id']);
            } else {
                this.setState({ display: true });
            }
        }).fail(() => this.setState({ display: true }));
    }

    render() {
        if (!this.state.display) {
            return <div></div>;
        }

        return (
            <div>
                <button onClick={() => this.submitRequest()}>
                    Request
                </button>
            </div>
        );
    }
}

export default SubmitGet;
