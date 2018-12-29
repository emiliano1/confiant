import React from 'react';
import reqwest from 'reqwest';

let int = 0;

class ShowId extends React.Component {
    constructor(props) {
        super(props);

        this.state = {
            pending: true,
            forecast_url: false,
            stations: [],
        };
    }

    componentDidUpdate() {
        // retry every 10 seconds until the result is ready
    }

    showId() {
        // Call /get/ + this.props.id
        // Use X-Auth-Token '88d72110d6c27f7d231c4c3197364ef0a17551c5'
        // and retrieve Json response

    }

    render() {
        if (!this.props.id) {
            return <div><h3>No Requests yet</h3></div>;
        }

        if (this.state.pending) {
            return (
                <div>
                    <h3>Pending</h3>
                    <div>{this.props.id}</div>
                </div>
            );
        } else {
            return (
                <div>
                    <h3>
                        <a href={this.state.forecast_url} target="_blank">
                            Weather
                        </a>
                    </h3>
                    <div>Temperature: {this.state.temp_f} °F</div>
                    <br />
                    <div>
                        {this.state.stations.map((c, i) => <div key={i}>{c.lat} &times; {c.lon}</div>)}
                    </div>
                </div>
            )
        }
    }
}

export default ShowId;

