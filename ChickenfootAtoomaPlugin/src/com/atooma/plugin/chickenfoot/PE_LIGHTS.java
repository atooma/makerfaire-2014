package com.atooma.plugin.chickenfoot;

import android.content.Context;
import android.os.RemoteException;

import com.atooma.plugin.ParameterBundle;
import com.atooma.plugin.Performer;
import com.loopj.android.http.AsyncHttpClient;

public class PE_LIGHTS extends Performer {

	public PE_LIGHTS(Context context, String id, int version) {
		super(context, id, version);
	}

	@Override
	public void declareParameters() {
		addParameter(R.string.address, R.string.address, "ADDRESS", "STRING", true);
		addParameter(R.string.duration, R.string.duration, "DURATION", "NUMBER", true);
	}

	@Override
	public ParameterBundle onInvoke(String ruleId, ParameterBundle parameters) throws RemoteException {
		String baseUrl = (String) parameters.get("ADDRESS");

		String url = baseUrl + "/api/action/lights/";

		AsyncHttpClient client = new AsyncHttpClient();
		client.post(url, null);
		return new ParameterBundle();
	}

	@Override
	public void defineUI() {
		setTitle(R.string.pe_lights);
		setIcon(R.drawable.plugin_icon_el_normal);
	}

}
