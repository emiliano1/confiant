import React from 'react';
import SubmitGet from './submit_get';
import ShowId from './show_id';

class App extends React.Component {
    constructor(props) {
        super(props);

        this.state = {
            id: null
        };
    }

    handle(id) {
        this.setState({ id });
    }

    render() {
        return (
            <div>
                <h1>Hello, World!</h1>
                <SubmitGet callback={id => this.handle(id)} />
                <ShowId id={this.state.id} />
            </div>
        );
    }
}

export default App;
