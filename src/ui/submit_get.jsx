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

        // Call /get/
        // Use X-Auth-Token '88d72110d6c27f7d231c4c3197364ef0a17551c5'
        // and callback with id
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
